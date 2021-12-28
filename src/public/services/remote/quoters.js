import { API_BASE_URL } from "../../utils/constants";
import { API_END_POINTS } from "../../utils/routes";

const getQuoters = async () => {
  console.log(API_BASE_URL + API_END_POINTS.quoters.getAllQuoters)
  const result = await fetch(
    API_BASE_URL + API_END_POINTS.quoters.getAllQuoters,
    {
      method: "GET",
    }
  );

  return result;
};

export { getQuoters };
