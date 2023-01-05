import { ThemeProvider } from "@emotion/react";
import { createTheme, CssBaseline } from "@mui/material";
import Routing from "../routing/Routes";
import Header from "./Header";

export default function App() {
  return (
    <ThemeProvider theme={createTheme({ palette: { mode: "dark" } })}>
      <CssBaseline />
      <div>
        <Header />
        <Routing />
      </div>
    </ThemeProvider>
  );
}
