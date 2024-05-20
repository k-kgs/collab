import { useState, useEffect } from "react";
import Router from "next/router";
import { getTaskList } from "../../services/task";
import { TaskCard } from "../../components/app/taskCard";

export function TaskListing() {
  const [myProject, setMyProject] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
    async function getList(e) {

        e.preventDefault();
        try {
                const payload = await getTaskList();
                const projectData = payload.data;
                if(projectData){
                    const myProjects = projectData
                    setMyProject(myProjects);
                    setIsLoading(false);
                }
            }
            catch (error) {
                console.log(error);
            } finally {
                setIsLoading(false);
            }
    }

    useEffect(() => {
            getList();
      }, []);

    return (
        <div disabled={isLoading}>
            {myProject.map((projectData)=>{
                return(
                <TaskCard data={projectData}/>
                )
            })}
        </div>
    )

}