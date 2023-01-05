import { Alert, AlertTitle } from "@mui/material";

export default function UrlError() {
  return (
    <Alert severity="error">
      <AlertTitle>Page Not Found :)</AlertTitle>
      The page you requested is not — <strong>found!</strong>
    </Alert>
  );
}
