import { useState } from "react";
import GlobalContext from "../context/GlobalContext";
import App from "../views/App";

export default function AppController() {
  const [message, setMessage] = useState("Loading ...");
  const [alertType, setAlertType] = useState("info");
  const [open, setOpen] = useState(false);

  const popup = (message, alertType) => {
    setMessage(message);
    setAlertType(alertType);
    setOpen(true);
  };

  return (
    <GlobalContext.Provider value={{ popup }}>
      <App
        message={message}
        alertType={alertType}
        open={open}
        setOpen={setOpen}
      />
    </GlobalContext.Provider>
  );
}
