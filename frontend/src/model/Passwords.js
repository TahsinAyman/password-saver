export default class Passwords {
  constructor(rowid, username, auth_password, content) {
    this.id = rowid;
    this.username = username;
    this.auth_password = auth_password;
    this.content = JSON.parse(content);
  }
  getId = () => this.id;
  getUsername = () => this.username;
  getAuth_Password = () => this.auth_password;
  getContent = () => this.content;
  setId(id) {
    this.id = id;
  }
  setUsername(username) {
    this.username = username;
  }
  setAuth_Password(auth_password) {
    this.auth_password = auth_password;
  }

  setContent(content) {
    this.content = content;
  }
} 