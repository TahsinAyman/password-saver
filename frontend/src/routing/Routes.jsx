import { Routes, Route } from "react-router-dom";
import HomeController from "../controller/HomeController";
import UrlError from "../views/UrlError";
import {
  RegisterController,
  LoginController,
} from "../controller/UserController";

export default function Routing() {
  return (
    <Routes>
      <Route path="/" element={<HomeController />} />
      <Route path="/register" element={<RegisterController />} />
      <Route path="/login" element={<LoginController />} />
      <Route path="/*" element={<UrlError />} />
    </Routes>
  );
}
