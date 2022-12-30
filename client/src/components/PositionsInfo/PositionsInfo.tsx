import React, { useState, useEffect } from 'react';
import DeleteDepartment from '../DeleteDepartment/DeleteDepartment';
import './PositionsInfo.css';

const PositionsInfo = () => {

  const [data, getData] = useState([])
  const URL = 'http://localhost:5000/api/v1/get_all_positions';

  useEffect(() => {
      fetchData()
  }, [])

  const fetchData = () => {
    fetch(URL)
      .then((res) =>
          res.json())
      .then((response) => {
          console.log(response.result);
          getData(response);
      })
  }

  return (
    <>
      <table className='table-positions'>
      <thead>
        <tr>
        <th>Отдел</th>
        <th>Зарплата(руб.)</th>
        <th>Должность</th>
        <th>Удалить должность</th>
        </tr>
      </thead>
      {data.map((item, i) => (
          <tr key={i}>
            <td>{item.department}</td>
            <td>{item.salary}</td>
            <td>{item.position}</td>
            <DeleteDepartment 
              id={item.id}
              position={item.position}
            />
            <br></br>
          </tr>
        ))}
      </table>
    </>
  )
}
export default PositionsInfo;