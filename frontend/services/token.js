export function removeToken() {
    localStorage.removeItem("collab_token");
    window.sessionStorage.removeItem("collab_token");
  }
  
  export function getToken() {
    return localStorage.getItem("collab_token") || window.sessionStorage.getItem("collab_token");
  }
  