import React from 'react'

const ModulePage = ({match}) => {
  
    let module_id = match.params.id

  
    return (
    <div>
        <h1>ModulePage {module_id}</h1>
    </div>
  )
}

export default ModulePage