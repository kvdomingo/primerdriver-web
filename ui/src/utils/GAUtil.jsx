import { useEffect } from "react";
import ReactGA from "react-ga4";
import { useLocation } from "react-router-dom";

const PROD = (process.env.NODE_ENV ?? "production") === "production";

function GAUtil() {
  const location = useLocation();

  if (PROD) {
    ReactGA.initialize("G-JDD7SXXVW0");
  }

  useEffect(() => {
    if (PROD) {
      ReactGA.send({
        hitType: "pageview",
        page: `${location.pathname}${location.search}`,
      });
    }
  }, [location.pathname, location.search]);

  return null;
}

export default GAUtil;
