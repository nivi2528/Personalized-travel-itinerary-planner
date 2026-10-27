function PlaceholderCard({ title, children }) {
  return (
    <article>
      <h3>{title}</h3>
      {children}
    </article>
  );
}

export default PlaceholderCard;
