import React, {useState, useEffect} from 'react'
import ListItem from '../components/ListItem'


const ModulesListPage = () => {
    let [modules, setModules] = useState([])
    
    useEffect(()=> {
        getModules()
    }, [])
    
    let getModules = async () => {
        let response = await fetch('/api/modules/')
        let data = await response.json()
        setModules(data)
    
    }

    return (
        <div>
            <div className='modules-list'>
                {modules.map((module, index) => (
                    <ListItem key={index} module={module} />
                ))}
            </div>
        </div>
    )
}

export default ModulesListPage