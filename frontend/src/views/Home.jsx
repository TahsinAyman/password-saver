import { Link } from "@mui/material";
import icon from "../resources/asset/images/icon.png";

export default function Home() {
  return (
    <>
      <div className="center">
        <img src={icon} alt="securify" height="500" />
        <br />
        <br />
        <Link href="/register">Join Now</Link>
      </div>
    </>
  );
}
