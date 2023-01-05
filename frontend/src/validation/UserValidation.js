import * as yup from "yup";

const validation = yup.object({
  username: yup
    .string()
    .required("Username is Reqiured")
    .min(3, "The Username Should Be At Least 3 characters")
    .max(10, "The Username Should Be Less then 10 characters"),
  auth_password: yup
    .string()
    .required("Password is reqiured")
    .min(3, "Password should at least be 3 characters"),
});

export default validation;