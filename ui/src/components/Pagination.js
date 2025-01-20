import React from 'react'

const Pagination = ({ page, totalPages, onPageChange }) => {
  return (
    <div className='pagination mt-4 flex items-center justify-between'>
      <button
        className='btn btn-secondary'
        onClick={() => onPageChange(page - 1)}
        disabled={page === 1}
      >
        Previous
      </button>
      <div className='page-numbers text-sm text-gray-600'>
        Page {page} of {totalPages}
      </div>
      <button
        className='btn btn-primary'
        onClick={() => onPageChange(page + 1)}
        disabled={page === totalPages}
      >
        Next
      </button>
    </div>
  )
}

export default Pagination
