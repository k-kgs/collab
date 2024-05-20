import { useState, useEffect } from "react";
import Router from "next/router";
import { getProjectList } from "../../services/project";
import { ProjectCard } from "../../components/app/projectCard";

export function ProjectListing() {
  const [myProject, setMyProject] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
    async function getList(e) {

        e.preventDefault();
        console.log("getList called")
        try {
                const payload = await getProjectList();
                const projectData = payload.data;
                if(projectData){
                    const myProjects = projectData.my_project
                    console.log("myProjects",myProjects);
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
                console.log("Calling from project:",projectData);
                return(
                <ProjectCard data={projectData}/>
                )
            })}
        </div>
    )

}