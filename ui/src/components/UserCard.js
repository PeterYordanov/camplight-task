import React from 'react'
import PropTypes from 'prop-types'

const UserCard = ({ user, onEdit, onDelete }) => {
  console.log(user)
  const avatarUrl = user.profile_photo
    ? `data:image/jpeg;base64,${user.profile_photo}`
    : '/images/default-avatar-icon.jpg'

  return (
    <div className='card card-bordered w-50 bg-base-100 shadow-md'>
      <div className='card-body p-4'>
        {/* Avatar */}
        <div className='avatar mb-2 flex justify-center'>
          <div
            className='w-16 h-16 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2 overflow-hidden'
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
          >
            <img
              src={avatarUrl}
              alt={`${user.first_name} ${user.last_name}`}
              className='object-cover'
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'cover',
                objectPosition: 'center'
              }}
            />
          </div>
        </div>
        {/* Name */}
        <h2
          className='card-title text-md font-semibold text-center'
          style={{
            margin: '4px 0'
          }}
        >
          {user.first_name} {user.last_name}
        </h2>
        {/* Email */}
        <p
          className='text-sm text-gray-600 text-center'
          style={{ margin: '2px 0' }}
        >
          {user.email}
        </p>
        {/* Phone number */}
        <p
          className='text-sm text-gray-600 text-center'
          style={{ margin: '2px 0' }}
        >
          {user.phone_number}
        </p>
        {/* Buttons */}
        <div className='flex justify-between mt-4'>
          <button
            className='btn btn-primary text-sm'
            onClick={() => onEdit(user)}
          >
            Edit
          </button>
          <button
            className='btn btn-error text-sm'
            onClick={() => onDelete(user.id)}
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  )
}

UserCard.propTypes = {
  user: PropTypes.object.isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired
}

export default UserCard
