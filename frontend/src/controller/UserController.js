import { useContext } from "react";
import GlobalContext from "../context/GlobalContext";
import { login, register } from "../service/UserService";
import Login from "../views/Login";
import Register from "../views/Register";

export function RegisterController() {
  const { popup } = useContext(GlobalContext);
  const onSubmit = (data) => {
    register(data, popup);
  };

  return <Register onSubmit={onSubmit} />;
}

export function LoginController() {
  const { popup } = useContext(GlobalContext);
  const onSubmit = (data) => {
    login(data, popup);
  };

  return <Login onSubmit={onSubmit} />;
}
