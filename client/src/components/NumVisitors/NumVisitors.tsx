import { useState, useEffect } from 'react';
import serverURL from '../../libs/serverApi';

const NumVisitors = () => {
  const [data, getData] = useState<any[]>([])
  const URL = serverURL + '/api/v1/num_visits';

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = () => {
    fetch(URL)
      .then((res) =>
        res.json())
      .then((response) => {
        getData(response);
      })
  }
  // @ts-ignore
  var visits = data["visited"]
  return (
    <div>
      Портал был посещён {visits} раз
    </div>
  )
}
export default NumVisitors;