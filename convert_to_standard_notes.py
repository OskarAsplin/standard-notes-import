from datetime import datetime
import json
import uuid

folder_path = "/PATH_TO_FOLDER/"
file_name = "notes.json" # needs to be json file
converted_file_name = "notes_converted.json"
tag_title = "todo" # add a relevant tag

file_path = folder_path + file_name
converted_file_path = folder_path + converted_file_name

result = {
  "items": [
    {
      "uuid": str(uuid.uuid4()),
      "content_type": "Tag",
      "content": {
        "title": tag_title,
        "references": []
      }
    }
  ]
}

with open(file_path, 'r') as file:
  notes = json.load(file)
  for note in notes:
    new_uuid = str(uuid.uuid4())
    result['items'][0]['content']['references'].append({ "content_type": "Note", "uuid": new_uuid })

    converted_note = {}
    converted_note['created_at'] = datetime.fromtimestamp(int(note['created'])/1000).isoformat()[:-3] + "Z"
    converted_note['updated_at'] = datetime.fromtimestamp(int(note['modified'])/1000).isoformat()[:-3] + "Z"
    converted_note['uuid'] = new_uuid
    converted_note['content_type'] = 'Note'
    converted_note['content'] = {
      "title": note['title'],
      "text": note['content'],
      "references": [],
      "appData": {
        "org.standardnotes.sn": {
          "client_updated_at": datetime.now().isoformat()[:-3] + "Z" # No idea if this appData part is necessary
        }
      }
    }

    result['items'].append(converted_note)

with open(converted_file_path, 'w+') as result_file:
  json.dump(result, result_file)
