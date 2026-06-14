class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self._content = content
        self.__audit_log = []
    
    def read(self) -> str:
        return self._content
    
    def history(self) -> tuple:
        return tuple(self.__audit_log)
    
    def _log(self, event: str) -> None:
        self.__audit_log.append(event)


class EditorDocument(Document):
    def edit(self, new_content: str) -> None:
        old_content = self._content
        self._content = new_content
        self._log(f"edit: {old_content} -> {new_content}")


class AdminDocument(EditorDocument):
    def purge_history(self) -> None:
        self._Document__audit_log.clear()



doc = AdminDocument("Spec", "v1")

print(doc.read())
doc.edit("v2")
doc.edit("v3")

print(doc.history())

doc.purge_history()
print(doc.history())
