import React, { useEffect, useState } from 'react'
import Typography from '../components/Typography'
import Health from '../services/Health'
import UsersList from '../components/UsersList'

export default function Home () {
  const [pingStatusCode, setPingStatusCode] = useState('')
  const [dbStatusCode, setDbStatusCode] = useState('')

  useEffect(() => {
    const checkServices = async () => {
      const pingResult = await Health.checkPing()
      setPingStatusCode(pingResult.status)

      const dbResult = await Health.checkDatabase()
      setDbStatusCode(dbResult.status)
    }

    checkServices()
  }, [])

  return (
    <Typography>
      <header style={{ marginBottom: '20px', textAlign: 'center' }}>
        <h1>Home Page</h1>
      </header>

      <section style={{ marginBottom: '20px' }}>
        <h4>
          Backend Service Status Code: <span>{pingStatusCode}</span>
          <br />
          Database Service Status Code: <span>{dbStatusCode}</span>
        </h4>
      </section>

      <section>
        <UsersList />
      </section>

    </Typography>
  )
}
