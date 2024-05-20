import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import { postProjectDetails } from "../../services/project";

export function ProjectForm({ data }) {
  useEffect(() => {
    if (JSON.stringify(data) != "{}") {
      setProjectData(data);
      setIsUpdate(true);
      setFormType("Update");
    }
  }, [data]);
  const [projectData, setProjectData] = useState({
    name: "",
    description: "",
    start_date: new Date().toISOString().slice(0, 10),
    estimated_delivery_date: new Date().toISOString().slice(0, 10),
  });
  const [isUpdate, setIsUpdate] = useState(false);
  const [formType, setFormType] = useState("Create");
  const defaultDate = new Date().toISOString().slice(0, 10);
  const descriptionHeight = 84;
  const handleLogin = async(e) => {
    e.preventDefault();
    const res = await postProjectDetails(projectData)
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProjectData({ ...projectData, [name]: value });
  };

  return (
    <form onSubmit={handleLogin}>
      <Box
        sx={{
          width: 400,
          display: "flex",
          alignItems: "center",
          flexDirection: "column",
          "& > :not(style)": { m: 1 },
        }}
      >
        <TextField
          label="Project Name"
          variant="outlined"
          fullWidth
          name="name"
          value={projectData.name}
          onChange={handleChange}
          required
        />
        <TextField
          label="Description"
          variant="outlined"
          multiline={true}
          rows={3}
          fullWidth
          name="description"
          value={projectData.description}
          onChange={handleChange}
          required
        />
        <TextField
          fullWidth
          label="Start Date"
          name="start_date"
          InputLabelProps={{ shrink: true, required: true }}
          type="date"
          value={projectData.start_date}
          onChange={handleChange}
          required
        />
        <TextField
          fullWidth
          label="Estimated Delivery Date"
          variant="outlined"
          name="estimated_delivery_date"
          InputLabelProps={{ shrink: true, required: true }}
          value={projectData.estimated_delivery_date}
          type="date"
          onChange={handleChange}
          required
        />
        <Button type="submit" variant="contained" fullWidth color="primary">
          {formType} Project
        </Button>
      </Box>
    </form>
  );
}

