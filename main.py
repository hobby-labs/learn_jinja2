#!/usr/bin/env python
import jinja2

class Main:
    def __init__(self):
        pass

    def exec(self):
        environment = jinja2.Environment()
        template = environment.from_string("Hello, {{ name }}")
        result = template.render(name="World")
        print(result)

if __name__ == "__main__":
    Main().exec()

