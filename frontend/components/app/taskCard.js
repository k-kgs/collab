import * as React from "react";
// import { styled } from "@mui/material/styles";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Avatar from "@mui/material/Avatar";
import IconButton, { IconButtonProps } from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import { red } from "@mui/material/colors";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import OpenWithIcon from "@mui/icons-material/OpenWith";
import Router from "next/router";

export function TaskCard(props) {
  const name= props.data.name;
  const nameFirstLetter= name.slice(0, 1)
  const handleExpandClick = () => {
    console.log("handleExpandClick");
  };
  const handleEditClick = (e) => {
    e.preventDefault();
    const url = "/app/createTask?task=" + props.data.id;
    Router.push(url)
  };

  return (
    <Card sx={{ maxWidth: 345, marginBottom:10}}>
      <CardHeader
        avatar={
          <Avatar sx={{ bgcolor: red[500] }} aria-label="recipe">
            {nameFirstLetter}
          </Avatar>
        }
        title={name}
        subheader={props.data.start_date}
      />
      <CardContent>
        <Typography variant="body2" color="text.secondary">
          {props.data.description}
        </Typography>
        <span> Deadline : {props.data.estimated_delivery_date}</span>
      </CardContent>
      <CardActions>
        <IconButton aria-label="add to favorites">
          <EditIcon onClick={handleEditClick}/>
        </IconButton>
        <IconButton aria-label="share">
          <DeleteIcon />
        </IconButton>
        <div style={{ marginRight: 160 }}></div>
        <IconButton aria-label="Open">
          <OpenWithIcon onClick={handleExpandClick} />
        </IconButton>
      </CardActions>
    </Card>
  );
}
