import { getToken } from "./token";
const base_url = 'http://localhost:8000'

export const loginUser = async (username, password) => {
  const res = await fetch(base_url + "/api/user/login", {
    headers: new Headers({'content-type': 'application/json'}),
    body: JSON.stringify({ 
        username: username,
        password: password
        }),
    method: "POST",
  });
  const data = await res.json();
  return data;
};
// ------------------------------------------------------------*
export const registerUser = async (payload) => {
  const res = await fetch(base_url + "/api/user/register", {
    headers: new Headers({'content-type': 'application/json'}),
    body: JSON.stringify(payload),
    method: "POST",
  });
  const data = await res.json();
  return data;
};
// ------------------------------------------------------------*
export const whoAmI = async () => {
  const res = await fetch(base_url + "/api/user/details", {
    headers: {
      authorization: "Token " + getToken(),
    },
    method: "GET",
  });
  const data = await res.json();
  return data;
};
