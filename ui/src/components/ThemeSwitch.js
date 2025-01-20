import React, { useEffect } from 'react'
import { Button } from 'react-daisyui'
import { themeChange } from 'theme-change'
import { MoonIcon } from '@heroicons/react/outline'

export default function ThemeSwitch (props) {
  useEffect(() => {
    themeChange(false)
  }, [])

  return (
    <div className='dropdown dropdown-end'>
      <label tabIndex='0' className='btn btn-ghost gap-3'>
        <div className='hidden md:block normal-case'>Theme</div>
        <MoonIcon className='h-6 w-6' />
      </label>
      <div
        tabIndex='0'
        className='menu dropdown-content rounded-box shadow-md bg-base-300 p-2 w-52 mt-[18px]'
      >
        {props.themes.map((theme) => {
          return (
            <Button
              key={theme.name}
              color='ghost'
              className='gap-3 justify-start normal-case'
              data-set-theme={theme.id}
            >
              {theme.icon}
              {theme.name}
            </Button>
          )
        })}
      </div>
    </div>
  )
}
