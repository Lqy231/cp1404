from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKmApp(App):
    def build(self):
        Window.size = (300, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self, value):
        try:
            result = float(value) * 1.60934
            self.root.ids.result.text = str(result)
        except ValueError:
            pass
    
    def up(self, value):
        try:
            result = float(value) + 1
            self.root.ids.input_number.text = str(result)
            self.convert(result)
        except ValueError:
            pass
    

    def down(self, value):
        try:
            result = float(value) - 1
            self.root.ids.input_number.text = str(result)
            self.convert(result)
        except ValueError:
            pass
        

ConvertMilesKmApp().run()
