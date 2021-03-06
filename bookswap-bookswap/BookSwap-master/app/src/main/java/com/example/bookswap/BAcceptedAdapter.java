package com.example.bookswap;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;


/**
 *  This is the BAccepteActivity adapter, can be using to display
 *  a list wait for owner agree to swap
 *
 */
public class BAcceptedAdapter extends ArrayAdapter<Book> {

    private ArrayList<Book> acceptList;

    /**
     * Constructor
     *
     * @param context  The current context.
     * @param resource The resource ID for a layout file containing a TextView to use when
     *                 instantiating views.
     * @param acceptList  The objects to represent in the ListView.
     */
    public BAcceptedAdapter(Context context, int resource,  ArrayList<Book> acceptList) {
        super(context, resource, acceptList);
        this.acceptList = acceptList;
    }

    /**
     * Get a View that displays the data at the specified position in the data set. You can either
     * create a View manually or inflate it from an XML layout file. When the View is inflated, the
     * parent View (GridView, ListView...) will apply default layout parameters unless you use
     * {@link LayoutInflater#inflate(int, ViewGroup, boolean)}
     * to specify a root view and to prevent attachment to the root.
     *
     * @param position    The position of the item within the adapter's data set of the item whose view
     *                    we want.
     * @param convertView The old view to reuse, if possible. Note: You should check that this view
     *                    is non-null and of an appropriate type before using. If it is not possible to convert
     *                    this view to display the correct data, this method can create a new view.
     *                    Heterogeneous lists can specify their number of view types, so that this View is
     *                    always of the right type (see {@link #getViewTypeCount()} and
     *                    {@link #getItemViewType(int)}).
     * @param parent      The parent that this view will eventually be attached to
     * @return A View corresponding to the data at the specified position.
     */
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        BAcceptedAdapter.ViewHolder holder = null;

        /**
         * about how to add a button into the listview item and how to using viewholder
         * i get the source from:https://blog.csdn.net/comeonyangzi/article/details/26858875
         */
        if (convertView == null){ // check if given view is null, if it is we inflate
            holder = new ViewHolder();
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.item_baccept, null);
            holder.title = (TextView) convertView.findViewById(R.id.listUsername);
            holder.author = (TextView) convertView.findViewById(R.id.listBookname);
            holder.bookcover = (ImageView)convertView.findViewById(R.id.bookCover);
            holder.button_swap = (Button)convertView.findViewById(R.id.ba_swap);
            convertView.setTag(holder);
        }
        else {
            holder = (ViewHolder)convertView.getTag();
        }

        Log.d("POSITION", Integer.toString(position));
        final Book element = acceptList.get(position);

        holder.title.setText((String)element.getTitle());
        holder.author.setText((String)element.getAuthor());
        holder.button_swap.setTag(position);

        holder.button_swap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent toSwapPage = new Intent(getContext(),BAcceptedSwapActivity.class);
                toSwapPage.putExtra("book",element);
                getContext().startActivity(toSwapPage);
            }
        });



        if (element.getImageUrl()!= null){
            Log.d("img","not null");
            Picasso.get()
                    .load(element.getImageUrl())
                    .into(holder.bookcover);
            }


        return convertView;
    }


    /**
     * builld ViewHolder
     */
    public final class ViewHolder {
        public TextView title;
        public TextView author;
        public ImageView bookcover;
        public Button button_swap;
    }








}
