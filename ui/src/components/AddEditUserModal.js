import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'

function AddEditUserModal ({ user, onSubmit, isOpen, toggleModal }) {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    phone_number: '',
    image: null
  })

  useEffect(() => {
    if (user) {
      setFormData({
        first_name: user.first_name || '',
        last_name: user.last_name || '',
        email: user.email || '',
        phone_number: user.phone_number || '',
        image: user.image || null
      })
    } else {
      setFormData({
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
        image: null
      })
    }
  }, [user])

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value || ''
    }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    onSubmit(formData)
    toggleModal()
  }

  return (
    <>
      <button className='btn btn-primary' onClick={toggleModal}>
        {user ? 'Edit User' : 'Add User'}
      </button>

      {isOpen && (
        <div className='modal modal-open'>
          <div className='modal-box relative'>
            <label htmlFor='my-modal' className='btn btn-sm btn-circle absolute right-2 top-2' onClick={toggleModal}>✕</label>
            <h3 className='text-lg font-bold'>{user ? 'Edit User' : 'Add New User'}</h3>
            <form onSubmit={handleSubmit} className='py-4'>
              <input
                type='text'
                name='first_name'
                placeholder='First Name'
                className='input input-bordered w-full mb-2'
                value={formData.first_name}
                onChange={handleChange}
                required
              />
              <input
                type='text'
                name='last_name'
                placeholder='Last Name'
                className='input input-bordered w-full mb-2'
                value={formData.last_name}
                onChange={handleChange}
                required
              />
              <input
                type='email'
                name='email'
                placeholder='Email'
                className='input input-bordered w-full mb-2'
                value={formData.email}
                onChange={handleChange}
                required
              />
              <input
                type='tel'
                name='phone_number'
                placeholder='Phone Number'
                className='input input-bordered w-full mb-2'
                value={formData.phone_number}
                onChange={handleChange}
                title='Please enter a valid phone number with at least 10 digits.'
                required pattern='\d{10,}'
              />
              <div className='modal-action'>
                <button type='submit' className='btn btn-primary'>
                  {user ? 'Update User' : 'Save User'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  )
}

AddEditUserModal.propTypes = {
  user: PropTypes.object,
  onSubmit: PropTypes.func.isRequired,
  isOpen: PropTypes.bool.isRequired,
  toggleModal: PropTypes.func.isRequired
}

export default AddEditUserModal
