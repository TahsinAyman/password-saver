import { ThemeProvider } from "@emotion/react";
import { createTheme, CssBaseline } from "@mui/material";
import Routing from "../routing/Routes";
import Header from "./Header";
import PopupDialog from "./PopupDialog";

export default function App(props) {
  return (
    <ThemeProvider theme={createTheme({ palette: { mode: "dark" } })}>
      <CssBaseline />
      <div>
        <Header />
        <Routing />
      </div>
      <PopupDialog
        open={props.open}
        setOpen={props.setOpen}
        message={props.message}
        alertType={props.alertType}
      />
    </ThemeProvider>
  );
}
