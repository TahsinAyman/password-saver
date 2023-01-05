export function login(user, popup) {
  if (user.username === "tahsin" && user.auth_password === "skyout123") {
    popup("Successfully Logged In", "success");
  } else {
    popup("Could not Log In", "error");
  }
}

export function register(user, popup) {
  if (user.username !== "tahsin") {
    popup("Successfully Registered", "success");
  } else {
    popup("Could not Register", "error");
  }
}
