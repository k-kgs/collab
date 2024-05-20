import React, { useState } from "react";
import Router from "next/router";
import { whoAmI } from "../../services/user";
import { removeToken } from "../../services/token";
// import { ProjectCard } from "../../components/app/projectCard"
import { ProjectListing } from "../../components/app/projectListing";

export default function Dashboard() {
  const [user, setUser] = useState({});
  // Watchers
  React.useEffect(() => {
    const token = localStorage.getItem("collab_token") || window.sessionStorage.getItem("collab_token");
    if (!token) {
      redirectToLogin();
    } else {
      (async () => {
        try {
          const payload = await whoAmI();
          if (payload.error === "Unauthorized") {
            // User is unauthorized and there is no way to support the User, it should be redirected to the Login page and try to logIn again.
            console.log("Not Authorized")
            redirectToLogin();
          } else {
            setUser(payload.data);
          }
        } catch (error) {
          // If we receive any error, we should be redirected to the Login page
          redirectToLogin();
        }
      })();
    }
  }, []);

  function redirectToLogin() {
    Router.push("/user/login");
  }

  function handleClick(e) {
    e.preventDefault();

    // removeToken();
    // redirectToLogin();
    Router.push("/app/createproject")
  }

  if (user.hasOwnProperty("username")) {
    return (
      <>
        <nav className="navbar navbar-light" style={{ backgroundColor: "#e3f2fd" }}>
          <div className="container-fluid">
            <a className="navbar-brand" href="#">
              Welcome {user.username}!
            </a>
            <button
              className="btn btn-info"
              type="button"
              style={{ color: "white", backgroundColor: "#0d6efd" }}
              onClick={handleClick}
            >
              Create Project
            </button>
          </div>
        </nav>
        <h3>{user.username}'s Projects</h3>
        {/* <ProjectCard/> */}
        <ProjectListing/>
      </>
    );
  }
  return <div>Welcome back soldier. Welcome to your empty profile.</div>;
}

// Fojan side notes :
// class A extends React.Component {
//     componentDidUpdate() {
//         React.useEffect(() => {

//         }) // with no second param
//     }
//     componentDidMount() {
//         React.useEffect(() => {

//         }, []) // the Second param should be empty
//     }
//     componentWillReceiveProps() {
//         React.useEffect(() => {

//         }, [props.name]) // The Second param is everything what you want
//     }
//     componentWillUnmount() {
//         React.useEffect(() => {
//             document.querySelectorAll("button").addEventListener("click", (e) => {

//             }, {})
//             return () => {
//                 // This function will be called before raise the Component's Destroy Event
//                 document.querySelectorAll("button").removeEventListener("click", (e) => {

//                 })
//             }
//         })
//     }
//     render() {
//         return (
//             <div>salam</div>
//         )
//     }
// }
