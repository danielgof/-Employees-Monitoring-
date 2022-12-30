import React, { useState, useEffect } from 'react';

const NumVisitors = () => {
  const [data, getData] = useState<any[]>([])
  const URL = 'http://127.0.0.1:5000/api/v1/num_visits';

  useEffect(() => {
    fetchData()
  }, [])
  
  const fetchData = () => {
    fetch(URL)
      .then((res) =>
          res.json())
      .then((response) => {
          // console.log(response.result);
          getData(response);
      })
  }

  return (
    <div>
      Портал был посещён {data['visited']} раз 
    </div>
  )
}
export default NumVisitors;