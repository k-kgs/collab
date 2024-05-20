import { getToken } from "./token";
const base_url = 'http://localhost:8000'

export const getProjectList = async () => {
  const res = await fetch(base_url + "/api/project/list", {
    headers: {
      authorization: "Token " + getToken(),
    },
    method: "GET",
  });
  const data = await res.json();
  return data;
};

export const getProjectDetails = async (project) => {
  const res = await fetch(base_url + "/api/project/?project=" + project, {
    headers: {
      authorization: "Token " + getToken(),
    },
    method: "GET",
  });
  const data = await res.json();
  return data;
};

export const postProjectDetails = async (project) => {
  const res = await fetch(base_url + "/api/project/", {
    headers: new Headers({
      'content-type': 'application/json',
      'authorization': "Token " + getToken(),
    }),
    body: JSON.stringify(project),
    method: "POST",
  });
  const data = await res.json();
  return data;
};
