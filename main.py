import arcade
'''
Раздел Констант
'''
WIN_WIDTH = 800
WIN_HEIGHT = 600
WIN_TITLE = 'BEST GAME 2022-2023-2024'
SPEED = 5
FPS = 10
GRAVITY = 1
'''
Класс Игры
'''
class Game(arcade.Window):
    def __init__(self):
        # Фунция отвечающая за инициализацию класса, и за настройку основных параметров.
        super().__init__(WIN_WIDTH, WIN_HEIGHT, WIN_TITLE)
        arcade.set_background_color(arcade.csscolor.AQUAMARINE)
    def Setup(self):
        # Функция определяющая основные настройки игры.


        # Создание Сцены
        self.scene = arcade.Scene()

        # Импорт карты
        lvl1_path = 'lvl1.json'

        # Указание слоя через который персонаж не может ходить

        layer_stop = {
            'main_layer': {
                'use_spatial_hash': True
            }
        }
        self.lvl1_map = arcade.load_tilemap(lvl1_path, 1, layer_stop)

        # Добавление карты на сцену

        self.scene = arcade.Scene.from_tilemap(self.lvl1_map)

        # Создание камеры
        self.main_camera = arcade.Camera()


        # Спрайт Героя
        self.main_hero_sprite = arcade.Sprite('hero.png', scale=0.16)
        self.main_hero_sprite.center_x = 150
        self.main_hero_sprite.center_y = 98
        self.scene.add_sprite('main_hero',self.main_hero_sprite)

        # Физический Движок
        self.physic_engine = arcade.PhysicsEnginePlatformer(self.main_hero_sprite,gravity_constant=GRAVITY,walls=self.scene['main_layer'])
    def on_key_press(self, symbol: int, modifiers: int):
        # Функция отвечающая за действия игры когда кнопка нажата.
        if symbol == arcade.key.UP or symbol == arcade.key.W:
            if self.physic_engine.can_jump():
                self.main_hero_sprite.change_y = SPEED + 10
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.main_hero_sprite.change_y = -(SPEED+10)
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.main_hero_sprite.change_x = SPEED
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.main_hero_sprite.change_x = -SPEED
    def on_key_release(self, symbol: int, modifiers: int):
        # Функция отвечающая за действия игры когда кнопки отжимаются.
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.main_hero_sprite.change_x = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.main_hero_sprite.change_x = 0
    def camera_to_player(self):
        """Функция которая перемещает камеру за игроком."""
        camera_center_x = self.main_hero_sprite.center_x - (self.main_camera.viewport_width / 2)
        camera_center_y = self.main_hero_sprite.center_y - (self.main_camera.viewport_height / 2)
        if camera_center_x < 0:
            camera_center_x = 0
        if camera_center_y < 0:
            camera_center_y = 0
        camera_view = camera_center_x,camera_center_y
        self.main_camera.move_to(camera_view,speed=0.1)

    def on_update(self, delta_time: FPS):
        # Функция отвечающая за обновление экрана.
        self.physic_engine.update()
        self.camera_to_player()
    def on_draw(self):
        # Функция отвечающая за отрисовку игры, и за очистку экрана.
        self.clear()
        self.main_camera.use()
        self.scene.draw()

'''
Объекты
'''
main = Game()
main.Setup()
arcade.run()