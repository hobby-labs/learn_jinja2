#!/usr/bin/env python
import jinja2

class Main:
    parameters = [
            {"name": "name01", "value": "value01"},
            {"name": "name02", "value": "value02"}
    ]

    def exec(self):
        environment = jinja2.Environment(loader=FileSystemLoader("."))
        environmen.get_template("template.j2")
        template.render()

if __name__ == "__main__":
    Main().exec()

