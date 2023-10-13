# Standard Notes Import
A Python script for creating a Standard Notes import file. Originally made for converting Huawei notes to Standard Notes import format, but can easily be adjusted to other formats.

Huawei notes had this format, where `created` and `modified` were Unix timestamps in milliseconds.

```json
[
  {
    "title": "Some title",
    "content": "Lorem ipsum dolor sit amet...",
    "created": 1697239900000,
    "modified": 1697239900000
  }
]
```
