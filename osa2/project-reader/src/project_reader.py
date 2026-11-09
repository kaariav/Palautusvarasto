
from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")

        data = toml.loads(content)
        project = data["project"]

        name = project["name"]
        description = project.get("description", "")
        license_name = project.get("license", "")

        authors = [
            author["name"] for author in project.get("authors", [])
        ]

        dependencies = [
            dependency.split(">=")[0]
            for dependency in project.get("dependencies", [])
        ]

        dev_dependencies = [
            dependency.split(">=")[0]
            for dependency in data.get("dependency-groups", {}).get("dev", [])
        ]

        return Project(
            name,
            description,
            dependencies,
            dev_dependencies,
            license_name,
            authors
        )
