# Standard Notes Import
A Python script for creating a Standard Notes import file. Originally made for converting Huawei notes to Standard Notes import format, but can easily be adjusted to other formats.

Huawei notes had this json format, where `created` and `modified` were Unix timestamps in milliseconds:

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

To convert your notes, adjust the values for `folder_path`, `file_name`, `converted_file_name`, `tag_title` in `convert_to_standard_notes.py` and then run: `python3 convert_to_standard_notes.py`

Your converted file should then have this json format which can be imported into Standard Notes:

```json
{
  "items":
  [
    {
      "uuid": "4d31c95d-3a60-4bf1-b994-5c97e5f36709",
      "content_type": "Tag",
      "content":
      {
        "title": "todo",
        "references":
        [
          {
            "content_type": "Note",
            "uuid": "bbf6f306-1ffa-4cf1-b864-bf657257cfff"
          }
        ]
      }
    },
    {
      "created_at": "2023-10-13T23:31:40.592Z",
      "updated_at": "2023-10-13T23:31:40.100Z",
      "uuid": "bbf6f306-1ffa-4cf1-b864-bf657257cfff",
      "content_type": "Note",
      "content":
      {
        "title": "Some title",
        "text": "Lorem ipsum dolor sit amet...",
        "references":
        [],
        "appData":
        {
          "org.standardnotes.sn":
          {
            "client_updated_at": "2023-10-14T01:50:45.331Z"
          }
        }
      }
    }
  ]
}
```
