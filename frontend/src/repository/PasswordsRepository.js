import Passwords from "../model/Passwords";

export function jsonToObj(json) {
  return new Passwords(
    json.rowid,
    json.username,
    json.auth_password,
    json.content
  );
}

export function objToJson(obj) {
  return {
    rowid: obj.getId(),
    username: obj.getUsername(),
    auth_password: obj.getPassword(),
    content: JSON.stringify(obj.getContent()),
  };
}

export function jsonListToObjList(jsonList) {
  var lst = [];
  jsonList.map((json) => {
    lst.push(
      new Passwords(json.rowid, json.username, json.auth_password, json.content)
    );
  });
  return lst;
}

export function objListToJsonList(objList) {
  var lst = [];
  objList.map((obj) => {
    lst.push({
      rowid: obj.getId(),
      username: obj.getUsername(),
      auth_password: obj.getPassword(),
      content: JSON.stringify(obj.getContent()),
    });
  });
  return lst;
}
