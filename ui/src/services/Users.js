import axios from 'axios'

const API_BASE_URL = 'http://localhost:9000'

const usersService = {
  fetchAll: async (page = 1, pageSize = 5) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/users/`, {
        params: { page, page_size: pageSize }
      })
      return response.data
    } catch (error) {
      handleServiceError(error)
    }
  },

  create: async (userData) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/users/`, userData)
      return response.data
    } catch (error) {
      handleServiceError(error)
    }
  },

  update: async (userId, userData) => {
    try {
      const response = await axios.put(`${API_BASE_URL}/users/${userId}`, userData)
      return response.data
    } catch (error) {
      handleServiceError(error)
    }
  },

  delete: async (userId) => {
    try {
      await axios.delete(`${API_BASE_URL}/users/${userId}`)
      return { message: 'User deleted successfully' }
    } catch (error) {
      handleServiceError(error)
    }
  }
}

function handleServiceError (error) {
  if (error.response) {
    throw new Error(error.response.data.detail || 'Failed to perform action')
  } else if (error.request) {
    throw new Error('No response from server. Please try again.')
  } else {
    throw new Error(error.message || 'An unexpected error occurred.')
  }
}

export default usersService
