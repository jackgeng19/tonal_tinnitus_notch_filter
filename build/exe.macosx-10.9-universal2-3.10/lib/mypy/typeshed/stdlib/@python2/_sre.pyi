from typing import Any, Iterable, Mapping, Sequence, overload

CODESIZE: int
MAGIC: int
MAXREPEAT: long
copyright: str

class SRE_Match(object):
    def start(self, group: int = ...) -> int: ...
    def end(self, group: int = ...) -> int: ...
    def expand(self, s: str) -> Any: ...
    @overload
    def group(self) -> str: ...
    @overload
    def group(self, group: int = ...) -> str | None: ...
    def groupdict(self) -> dict[int, str | None]: ...
    def groups(self) -> tuple[str | None, ...]: ...
    def span(self) -> tuple[int, int]: ...
    @property
    def regs(self) -> tuple[tuple[int, int], ...]: ...  # undocumented

class SRE_Scanner(object):
    pattern: str
    def match(self) -> SRE_Match: ...
    def search(self) -> SRE_Match: ...

class SRE_Pattern(object):
    pattern: str
    flags: int
    groups: int
    groupindex: Mapping[str, int]
    indexgroup: Sequence[int]
    def findall(self, source: str, pos: int = ..., endpos: int = ...) -> list[tuple[Any, ...] | str]: ...
    def finditer(self, source: str, pos: int = ..., endpos: int = ...) -> Iterable[tuple[Any, ...] | str]: ...
    def match(self, pattern, pos: int = ..., endpos: int = ...) -> SRE_Match: ...
    def scanner(self, s: str, start: int = ..., end: int = ...) -> SRE_Scanner: ...
    def search(self, pattern, pos: int = ..., endpos: int = ...) -> SRE_Match: ...
    def split(self, source: str, maxsplit: int = ...) -> list[str | None]: ...
    def sub(self, repl: str, string: str, count: int = ...) -> tuple[Any, ...]: ...
    def subn(self, repl: str, string: str, count: int = ...) -> tuple[Any, ...]: ...

def compile(
    pattern: str,
    flags: int,
    code: list[int],
    groups: int = ...,
    groupindex: Mapping[str, int] = ...,
    indexgroup: Sequence[int] = ...,
) -> SRE_Pattern: ...
def getcodesize() -> int: ...
def getlower(a: int, b: int) -> int: ...