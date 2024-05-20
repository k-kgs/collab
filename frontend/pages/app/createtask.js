import React, { useState } from "react";
import Router from "next/router";
import { whoAmI } from "../../services/user";
import { removeToken } from "../../services/token";
import {getTaskDetails} from "../../services/task"
import { TaskForm } from "../../components/app/TaskForm";

export default function CreateTroject() {
  const [user, setUser] = useState({});
  const [projectData, setProjectData] = useState({})
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
            console.log("Not Authorized")
            redirectToLogin();
          } else {
            debugger;
            setUser(payload.data);
            const params = new URL(document.location.toString()).searchParams;
            const projectId = params.get('project', null);
            console.log("projectId",projectId)
            if(projectId){
                const data = await getTaskDetails(projectId)
                console.log("data from createProject",data)
                setProjectData(data.data)
            }
          }
        } catch (error) {
            console.log("error",error)
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
    Router.push("/app/taskboard")
  }

  function handleLogout(e) {
    e.preventDefault();

    removeToken();
    redirectToLogin();
  }

  if (user.hasOwnProperty("username") && projectData != {}) {
    return (
      <>
        <nav className="navbar navbar-light" style={{ backgroundColor: "#e3f2fd" }}>
          <div className="container-fluid">
          <button
              className="btn btn-info"
              type="button"
              style={{ color: "white", backgroundColor: "#0d6efd" }}
              onClick={handleClick}
            >
              Taskboard
            </button>
            <span>Create/Edit your Task</span>
            <button
              className="btn btn-info"
              type="button"
              style={{ color: "white", backgroundColor: "#0d6efd" }}
              onClick={handleLogout}
            >
              Logout
            </button>
          </div>
        </nav>
        <div style={{
            display: "flex",
            alignItems: "center",
            flexDirection: "column",
        }}
        ><TaskForm data={projectData}/></div>
      </>
    );
  }
  return <div>Welcome back soldier. Welcome to your empty profile.</div>;
}

