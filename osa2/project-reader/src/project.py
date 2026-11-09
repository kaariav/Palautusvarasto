

class Project:
    def __init__(
        self,
        name,
        description,
        dependencies,
        dev_dependencies,
        license_name,
        authors
    ):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license_name
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return "\n".join(f"- {d}" for d in dependencies) if dependencies else "-"

    def __str__(self):
        authors = "\n".join(f"- {author}" for author in self.authors)

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n{authors or '-'}"
            f"\n\nDependencies:\n{self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
