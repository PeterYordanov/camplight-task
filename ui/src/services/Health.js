import axios from 'axios'

const API_BASE_URL = 'http://localhost:9000'

const healthService = {
  checkPing: async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/health/ping`)
      return {
        status: response.status,
        data: response.data
      }
    } catch (error) {
      console.error('Error during checkPing:', error)
      return {
        status: error.response?.status || 500,
        error: error.message
      }
    }
  },

  checkDatabase: async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/health/test-database`)
      return {
        status: response.status,
        data: response.data
      }
    } catch (error) {
      console.error('Error during checkDatabase:', error)
      return {
        status: error.response?.status || 500,
        error: error.message
      }
    }
  }
}

export default healthService
