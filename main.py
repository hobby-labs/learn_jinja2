#!/usr/bin/env python
import jinja2
from jinja2 import Environment, FileSystemLoader

class Main:
    parameters = [
            {"name": "name01", "value": "value01"},
            {"name": "name02", "value": "value02"}
    ]

    def exec(self):
        environment = jinja2.Environment(loader=FileSystemLoader("."))
        template = environment.get_template("template.j2")
        print(template.render(parameters = self.parameters))

if __name__ == "__main__":
    Main().exec()

