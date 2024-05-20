import { getToken } from "./token";
const base_url = 'http://localhost:8000'

export const getTaskList = async (project) => {
  const res = await fetch(base_url + "/api/task/list?project_id=" + project, {
    headers: {
      authorization: "Token " + getToken(),
    },
    method: "GET",
  });
  const data = await res.json();
  return data;
};

export const getTaskDetails = async (task) => {
  const res = await fetch(base_url + "/api/task/?task=" + task, {
    headers: {
      authorization: "Token " + getToken(),
    },
    method: "GET",
  });
  const data = await res.json();
  return data;
};

export const postTaskDetails = async (task) => {
  const res = await fetch(base_url + "/api/task/", {
    headers: new Headers({
      'content-type': 'application/json',
      'authorization': "Token " + getToken(),
    }),
    body: JSON.stringify(task),
    method: "POST",
  });
  const data = await res.json();
  return data;
};
