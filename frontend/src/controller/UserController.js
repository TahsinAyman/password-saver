import { useContext } from "react";
import GlobalContext from "../context/GlobalContext";
import { login, register } from "../service/UserService";
import Login from "../views/Login";
import Register from "../views/Register";

export function RegisterController() {
  const onSubmit = (data) => {
    register(data, popup);
  };

  const { popup } = useContext(GlobalContext);

  return <Register onSubmit={onSubmit} />;
}

export function LoginController() {
  const onSubmit = (data) => {
    login(data, popup);
  };

  const { popup } = useContext(GlobalContext);

  return <Login onSubmit={onSubmit} />;
}
