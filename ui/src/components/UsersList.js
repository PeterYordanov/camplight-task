import React, { useEffect, useState } from 'react'
import UserCard from './UserCard'
import usersService from '../services/Users'
import AddEditUserModal from '../components/AddEditUserModal'
import Pagination from '../components/Pagination'

const UsersList = () => {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [page, setPage] = useState(1)
  const [pageSize] = useState(6)
  const [totalCount, setTotalCount] = useState(null)
  const [currentUser, setCurrentUser] = useState(null)
  const [showSavedToast, setShowSavedToast] = useState(false)
  const [showDeletedToast, setShowDeletedToast] = useState(false)
  const [isModalOpen, setIsModalOpen] = useState(false)

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true)
        const response = await usersService.fetchAll(page, pageSize)
        console.log(response)
        console.log(response.data)
        setUsers(response.data)
        setTotalCount(response.total_count)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    fetchUsers()
  }, [page, pageSize])

  const handleUserSubmit = async (userData) => {
    try {
      setShowSavedToast(false)
      let response
      if (currentUser) {
        response = await usersService.update(currentUser.id, userData)
        console.log('Updated user:', response)
        setUsers(users.map(user => user.id === currentUser.id ? { ...user, ...userData } : user))
      } else {
        response = await usersService.create(userData)
        console.log('Added new user:', response)
        setUsers([...users, response.data])
      }
      setShowSavedToast(true)
      setTimeout(() => {
        setShowSavedToast(false)
        toggleModal()
      }, 3000)
    } catch (error) {
      console.error('Error saving user:', error)
      setError(error.message)
    }
  }

  const handleEdit = (user) => {
    console.log('Editing user:', user)
    setCurrentUser(user)
    setIsModalOpen(true)
  }

  const handleDelete = async (userId) => {
    console.log('Deleting user with ID:', userId)
    try {
      await usersService.delete(userId)
      setUsers(users.filter((user) => user.id !== userId))

      setShowDeletedToast(true)

      setTimeout(() => {
        setShowDeletedToast(false)
      }, 3000)
    } catch (error) {
      console.error('Error deleting user:', error)
    }
  }

  const handlePageChange = (newPage) => {
    setPage(newPage)
  }

  const toggleModal = () => {
    setIsModalOpen(!isModalOpen)
    setCurrentUser(null)
  }

  if (loading) {
    return <p>Loading users...</p>
  }

  if (error) {
    return <p className='text-error'>Error: {error}</p>
  }

  const totalPages = Math.ceil(totalCount / pageSize)

  return (
    <div className='users-list'>
      <div className='flex items-center justify-between mb-4'>
        <h1 className='text-2xl font-bold'>Users List</h1>
        <AddEditUserModal user={currentUser} onSubmit={handleUserSubmit} isOpen={isModalOpen} toggleModal={toggleModal} />
      </div>

      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'>
        {users.length > 0
          ? (
              users.map((user) => <UserCard key={user.id} user={user} onEdit={handleEdit} onDelete={handleDelete} />)
            )
          : (
            <p>No users found.</p>
            )}
      </div>

      <Pagination page={page} totalPages={totalPages} onPageChange={handlePageChange} />

      {/* Toast notifications */}
      {showSavedToast && (
        <div className='toast toast-top toast-center w-64'>
          <div className='alert alert-success'>
            <span>User saved successfully!</span>
          </div>
        </div>
      )}

      {showDeletedToast && (
        <div className='toast toast-top toast-center w-64'>
          <div className='alert alert-success'>
            <span>User deleted successfully!</span>
          </div>
        </div>
      )}
    </div>
  )
}

export default UsersList
