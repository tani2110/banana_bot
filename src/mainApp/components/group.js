import React from "react";
import './group.css';
import { Link } from 'react-router-dom';
import { Navigate, useNavigate } from "react-router-dom";


function Group() {
    const navigate = useNavigate();
  return( 
    <div className="lessgo">
    <div className="b">
        <button className="btn" onClick={() => {
              navigate("/group1");}} >group1</button>
    </div>
    <div className="b"> <button className="btn">group2</button></div>
    <div className="b"> <button className="btn">math</button></div>
    </div>
);
};

export default Group;
