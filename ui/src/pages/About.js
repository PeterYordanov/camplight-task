import React from 'react'
import Typography from '../components/Typography'

export default function About () {
  return (
    <Typography component='div'>
      <h1>About this project</h1>
      <p>This project is designed using a React frontend coupled with a FastAPI backend and utilizes a PostgreSQL database for data management.</p>
      <p>The system supports full CRUD operations on users, includes health checking services, and integrates security measures such as CORS and input validation with Pydantic.</p>
      <p>Deployment is managed locally using Docker compose, ensuring consistent environments and easy setup.</p>
      {/* If you have links here, make sure to include rel="noopener noreferrer" when using target="_blank" */}
      - <a href='https://reactjs.org/' target='_blank' rel='noopener noreferrer'>Learn more about React</a><br />
      - <a href='https://fastapi.tiangolo.com/' target='_blank' rel='noopener noreferrer'>Learn more about FastAPI</a><br />
      - <a href='https://www.postgresql.org/' target='_blank' rel='noopener noreferrer'>Learn more about PostgreSQL</a><br />
      - <a href='https://www.docker.com/' target='_blank' rel='noopener noreferrer'>Learn more about Docker</a><br />
    </Typography>
  )
}
